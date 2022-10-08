data =dlmread('../data/cluster_data.txt',' ');
size(data)
## Perform clustering
[idx, centers] = kmeans (data, 2);

## Plot the result
figure
plot (data (idx==1, 1), data (idx==1, 2), 'ro');
hold on
plot (data (idx==2, 1), data (idx==2, 2), 'bs');
plot (centers (:, 1), centers (:, 2), 'kv', 'markersize', 10);
hold off
