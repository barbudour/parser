# ICardSchemeInfoProvider - методы
##  __Методы
[CreateForCardType](M_Tessa_Cards_ICardSchemeInfoProvider_CreateForCardType.htm)|
Создает экземпляр
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm),
содержащий таблицы из основной схемы и виртуальной схемы типа карточки
cardType.  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[EnsureCacheResolvedAsync](M_Tessa_Cards_ICardSchemeInfoProvider_EnsureCacheResolvedAsync.htm)|
Заполняет внутренний кэш объекта, если он используется.  
[GetTableAsync](M_Tessa_Cards_ICardSchemeInfoProvider_GetTableAsync.htm)|
Возвращает таблицу по идентификатору. Выбрасывает исключение, если таблица не
найдена.  
[GetTablesAsync](M_Tessa_Cards_ICardSchemeInfoProvider_GetTablesAsync.htm)|
Получает все таблицы, доступные в рамках схемы данных текущего объекта.  
[InvalidateCache](M_Tessa_Cards_ICardSchemeInfoProvider_InvalidateCache.htm)|
Сбрасывает кэш в текущем объекте.  
[TryGetTableAsync](M_Tessa_Cards_ICardSchemeInfoProvider_TryGetTableAsync.htm)|
Возвращает таблицу по идентификатору или null, если таблица не найдена.  
## __Методы расширения
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_1.htm)|
Выполняет проверку наличия таблицы с идентификатором tableID в схеме.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
---|---  
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync.htm)|
Выполняет проверку наличия колонки с идентификатором columnID в таблице с
идентификатором tableID.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[ICardSchemeInfoProvider - ](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
