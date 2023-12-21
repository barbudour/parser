# CreateCardAsyncFunc - делегат
Делегат для перегрузки действия [CreateCardAsync(Nullable<Guid>, String,
CreateCardOptions, CancellationToken)](M_Tessa_UI_IUIHost_CreateCardAsync.htm)
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<IUIContextObject> CreateCardAsyncFunc(
    	Guid? cardTypeID = null,
    	string cardTypeName = null,
    	CreateCardOptions options = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function CreateCardAsyncFunc ( 
    	Optional cardTypeID As Guid? = Nothing,
    	Optional cardTypeName As String = Nothing,
    	Optional options As CreateCardOptions = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IUIContextObject)
C++ __Копировать
     public delegate Task<IUIContextObject^>^ CreateCardAsyncFunc(
    	Nullable<Guid> cardTypeID = nullptr, 
    	String^ cardTypeName = nullptr, 
    	CreateCardOptions^ options = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type CreateCardAsyncFunc = 
        delegate of 
            ?cardTypeID : Nullable<Guid> * 
            ?cardTypeName : string * 
            ?options : CreateCardOptions * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardTypeID = defaultArg cardTypeID null
            let _cardTypeName = defaultArg cardTypeName null
            let _options = defaultArg options null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IUIContextObject>
#### Параметры
cardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
options [CreateCardOptions](T_Tessa_UI_CreateCardOptions.htm) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IUIContextObject](T_Tessa_UI_IUIContextObject.htm)>
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
