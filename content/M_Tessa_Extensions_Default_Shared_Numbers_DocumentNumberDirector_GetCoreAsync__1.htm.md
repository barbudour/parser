# DocumentNumberDirector.GetCoreAsync<T> \- метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<Object> GetCoreAsync<T>(
    	INumberContext context,
    	Object parameter = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function GetCoreAsync(Of T) ( 
    	context As INumberContext,
    	Optional parameter As Object = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Object)
C++ __Копировать
     public:
    generic<typename T>
    virtual ValueTask<Object^> GetCoreAsync(
    	INumberContext^ context, 
    	Object^ parameter = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetCoreAsync : 
            context : INumberContext * 
            ?parameter : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parameter = defaultArg parameter null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Object> 
    override GetCoreAsync : 
            context : INumberContext * 
            ?parameter : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parameter = defaultArg parameter null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Object> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
parameter [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Параметры типа
T
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
