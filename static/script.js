document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.fridgeTr').forEach(function (item) {
        item.onclick = () => {

            const request = new XMLHttpRequest();
            request.open('POST', '/add_click');

            request.onload = () => {
                const data = JSON.parse(request.responseText);
                let thClicks = item.children[1];
                thClicks.innerHTML = data.clicks
            };
            const data = new FormData();
            data.append('id', item.id);
            data.append('type', 'fridge');

            request.send(data);
            return false;
        };
    });

    document.querySelectorAll('.televisorTr').forEach(function (item) {
        item.onclick = () => {

            const request = new XMLHttpRequest();
            request.open('POST', '/add_click');

            request.onload = () => {
                const data = JSON.parse(request.responseText);
                let thClicks = item.children[1];
                thClicks.innerHTML = data.clicks
            };
            const data = new FormData();
            data.append('id', item.id);
            data.append('type', 'televisor');

            request.send(data);
            return false;
        };
    })
});
