# OpenCardAsyncFunc - делегат
Делегат для перегрузки действия [OpenCardAsync(Nullable<Guid>, Nullable<Guid>,
String, OpenCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_OpenCardAsync.htm)
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<IUIContextObject> OpenCardAsyncFunc(
    	Guid? cardID = null,
    	Guid? cardTypeID = null,
    	string cardTypeName = null,
    	OpenCardOptions options = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function OpenCardAsyncFunc ( 
    	Optional cardID As Guid? = Nothing,
    	Optional cardTypeID As Guid? = Nothing,
    	Optional cardTypeName As String = Nothing,
    	Optional options As OpenCardOptions = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IUIContextObject)
C++ __Копировать
     public delegate Task<IUIContextObject^>^ OpenCardAsyncFunc(
    	Nullable<Guid> cardID = nullptr, 
    	Nullable<Guid> cardTypeID = nullptr, 
    	String^ cardTypeName = nullptr, 
    	OpenCardOptions^ options = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type OpenCardAsyncFunc = 
        delegate of 
            ?cardID : Nullable<Guid> * 
            ?cardTypeID : Nullable<Guid> * 
            ?cardTypeName : string * 
            ?options : OpenCardOptions * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardID = defaultArg cardID null
            let _cardTypeID = defaultArg cardTypeID null
            let _cardTypeName = defaultArg cardTypeName null
            let _options = defaultArg options null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IUIContextObject>
#### Параметры
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
cardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
options [OpenCardOptions](T_Tessa_UI_OpenCardOptions.htm) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IUIContextObject](T_Tessa_UI_IUIContextObject.htm)>
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
