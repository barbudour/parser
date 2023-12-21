# DocumentNumberDirector.IsUsingNumberSystemAsync - метод
Возвращает признак того, что для карточки разрешено использование номеров.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected ValueTask<bool> IsUsingNumberSystemAsync(
    	INumberContext context,
    	Func<CancellationToken, ValueTask<IKrType>> getKrTypeAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Function IsUsingNumberSystemAsync ( 
    	context As INumberContext,
    	getKrTypeAsync As Func(Of CancellationToken, ValueTask(Of IKrType)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    ValueTask<bool> IsUsingNumberSystemAsync(
    	INumberContext^ context, 
    	Func<CancellationToken, ValueTask<IKrType^>>^ getKrTypeAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member IsUsingNumberSystemAsync : 
            context : INumberContext * 
            getKrTypeAsync : Func<CancellationToken, ValueTask<IKrType>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
getKrTypeAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IKrType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrType.htm)>>
     Асинхронная функция, возвращающая тип карточки или документа из типового решения. Может быть равен null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если для карточки разрешено использование номеров; false в противном
случае.
## __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
