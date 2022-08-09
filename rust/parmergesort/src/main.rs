use std::collections::vec_deque::VecDeque;
use std::thread;
use std::time::Instant;

fn parmergesort<T: Ord + Send + Clone>(seq: &mut [T], p: usize) {
    assert_ne!(p, 0);

    if seq.len() == 1 {
        return;
    }

    let p = if p.is_power_of_two() {
        p
    } else {
        p.next_power_of_two() / 2
    };

    let middle = (seq.len() - 1) / 2;

    let (mut left, mut right) = seq.split_at_mut(middle + 1);
    if p > 1 {
        thread::scope(|s| {
            s.spawn(|| {
                parmergesort(&mut left, p / 2);
            });

            s.spawn(|| {
                parmergesort(&mut right, p / 2);
            });
        })
    } else {
        parmergesort(&mut left, p);
        parmergesort(&mut right, p);
    }
    merge(&mut left, &mut right);
}

fn merge<T: Ord + Send + Clone>(left: &mut [T], right: &mut [T]) {
    let mut buf1 = VecDeque::from_iter(left.iter().cloned());
    let mut buf2 = VecDeque::from_iter(right.iter().cloned());

    let mut i = 0;
    while !buf1.is_empty() && !buf2.is_empty() {
        if buf1[0] <= buf2[0] {
            if i < left.len() {
                left[i] = buf1.pop_front().unwrap();
            } else {
                right[i - left.len()] = buf1.pop_front().unwrap();
            }
        } else {
            if i < left.len() {
                left[i] = buf2.pop_front().unwrap();
            } else {
                right[i - left.len()] = buf2.pop_front().unwrap();
            }
        }
        i += 1
    }

    while !buf1.is_empty() {
        if i < left.len() {
            left[i] = buf1.pop_front().unwrap();
        } else {
            right[i - left.len()] = buf1.pop_front().unwrap();
        }
        i += 1;
    }

    while !buf2.is_empty() {
        if i < left.len() {
            left[i] = buf2.pop_front().unwrap();
        } else {
            right[i - left.len()] = buf2.pop_front().unwrap();
        }
        i += 1;
    }
}

fn main() {
    let seq: Vec<i32> = [1, 3, 7, 2, -1, 4, 5, 8, 3164824, -176349]
        .iter()
        .cycle()
        .take(20_000_000)
        .copied()
        .collect();

    println!("n = {}", seq.len());
    let mut baseline = seq.clone();
    let now = Instant::now();
    baseline.sort();
    let baseline_elapsed = now.elapsed().as_secs_f64();
    println!("baseline_elapsed = {baseline_elapsed:.3} s");

    for p in [1, 2, 4, 8] {
        let mut seq = seq.clone();
        let now = Instant::now();
        parmergesort(&mut seq, p);
        assert_eq!(seq, baseline);
        let elapsed = now.elapsed().as_secs_f64();
        println!(
            "threads = {p}, elapsed = {:.3} s ({:.3}x baseline)",
            elapsed,
            elapsed / baseline_elapsed
        );
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let seq: Vec<i32> = [1, 3, 7, 2, -1, 4, 5, 8, 3164824]
            .iter()
            .cycle()
            .take(99)
            .copied()
            .collect();

        let mut baseline = seq.clone();
        baseline.sort();

        for p in [1, 2, 4, 8] {
            let mut seq = seq.clone();
            parmergesort(&mut seq, p);
            assert_eq!(seq, baseline);
        }
    }
}
