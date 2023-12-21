# DocumentNumberDirector.OnSavingNewCardAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task<bool> OnSavingNewCardAsync(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function OnSavingNewCardAsync ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ OnSavingNewCardAsync(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract OnSavingNewCardAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override OnSavingNewCardAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
