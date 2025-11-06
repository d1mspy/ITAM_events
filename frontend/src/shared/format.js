export function fromatRuData(iso) {
    const d = new Date(iso);
    return d.toLocaleDateString('ru-RU', {
        day: 'numeric',
        month: 'long'
    });
}

export function formatTimeRange(startIso, endIso) {
    const start = new Date(startIso);
    const end = new Date(endIso);

    const to2 = (n) => String(n).padStart(2, '0');
    const sH = to2(start.getHours()), sM = to2(start.getMinutes());
    const eH = to2(end.getHours()), eM = to2(end.getMinutes());

    return `${sH}:${sM}-${eH}:${eM}`;
}

export function getEventStatus(startIso, endIso) {
    const now = new Date();
    const start = new Date(startIso);
    const end = new Date(endIso);

    if (end < now) {
        return 'past';
    } 
    if (start <= now && now <= end) {
        return 'active';
    } 
    return 'upcoming'; 

}