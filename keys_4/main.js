function isLeapYear(year) {
        return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    }

    function daysUntilNewYear(date) {
        const year = date.getFullYear();
        const newYearDate = new Date(year, 11, 31);
        const diffMs = newYearDate - date;
        return Math.ceil(diffMs / (1000 * 60 * 60 * 24));
    }

    document.getElementById('calcBtn').addEventListener('click', () => {
        const inputValue = document.getElementById('dateInput').value;

        if (!inputValue) {
            alert('Выберите дату!');
            return;
        }

        const date = new Date(inputValue);
        const year = date.getFullYear();

        document.getElementById('daysResult').textContent = 
            `До Нового года осталось: ${daysUntilNewYear(date)} дней`;

        document.getElementById('leapResult').textContent = 
            isLeapYear(year) ? 'Високосный год' : 'Не високосный год';
    });