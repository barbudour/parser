# NumberExtensions.ReserveAcquiredNumberAsync - метод
Резервирует номер, который ранее мог быть выделен и который указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращает признак того, что номер успешно зарезервирован.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> ReserveAcquiredNumberAsync(
    	this INumberComposer composer,
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ReserveAcquiredNumberAsync ( 
    	composer As INumberComposer,
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<bool>^ ReserveAcquiredNumberAsync(
    	INumberComposer^ composer, 
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ReserveAcquiredNumberAsync : 
            composer : INumberComposer * 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
composer [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)
    Объект, обрабатывающий логику выделения и изменения номеров карточки.
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером, в котором указывается номер.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если номер, указанный в объекте context, успешно зарезервирован; false в
противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
