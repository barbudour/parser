# ICardSchemeInfoProvider.GetTableAsync - метод
Возвращает таблицу по идентификатору. Выбрасывает исключение, если таблица не
найдена.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<SchemeTable> GetTableAsync(
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetTableAsync ( 
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeTable)
C++ __Копировать
     ValueTask<SchemeTable^> GetTableAsync(
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetTableAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор таблицы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>  
Запрошенная таблица.
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Таблица не найдена по запрошенному идентификатору.  
---|---  
##  __См. также
#### Ссылки
[ICardSchemeInfoProvider - ](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
