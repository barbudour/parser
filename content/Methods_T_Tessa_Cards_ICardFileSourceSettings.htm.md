# ICardFileSourceSettings - методы
##  __Методы
[GetAllAsync](M_Tessa_Cards_ICardFileSourceSettings_GetAllAsync.htm)| Все
доступные местоположения.  
---|---  
[GetAsync](M_Tessa_Cards_ICardFileSourceSettings_GetAsync.htm)|  Возвращает
информацию по местоположению файлов для заданного типа местоположения.
Возвращённый объект гарантированно не равен null. Если информации по
местоположению не найдено, то выбрасывается исключение
[System.Collections.Generic.KeyNotFoundException].  
[GetDefaultAsync](M_Tessa_Cards_ICardFileSourceSettings_GetDefaultAsync.htm)|
Местоположение по умолчанию. Может быть равно null только в том случае, если в
системе не зарегистрировано ни одного местоположения.  
[GetLargeFileSizeAsync](M_Tessa_Cards_ICardFileSourceSettings_GetLargeFileSizeAsync.htm)|
Начальный размер файла в байтах, который считается большим файлом, поэтому для
него может быть доступна особая обработка на клиенте, или null, если файлы
любого размера не считаются большими. Свойство может использоваться на клиенте
и на сервере.  
[GetMaxFileSizeAsync](M_Tessa_Cards_ICardFileSourceSettings_GetMaxFileSizeAsync.htm)|
Максимальный размер файла в байтах, для которого разрешена загрузка в систему,
или null, если ограничения по размеру отсутствует. Свойство может
использоваться на клиенте и на сервере.  
[SetCachingSourceAsync](M_Tessa_Cards_ICardFileSourceSettings_SetCachingSourceAsync.htm)|
Устанавливает источник получения настроек по местоположению файлов.  
[TryGetAsync](M_Tessa_Cards_ICardFileSourceSettings_TryGetAsync.htm)|
Возвращает информацию по местоположению файлов для заданного типа
местоположения или null, если в системе не задано информации для заданного
типа.  
## __См. также
#### Ссылки
[ICardFileSourceSettings - ](T_Tessa_Cards_ICardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
