# NumberExtensions.AcquireNumberByTypeAsync - метод
Выделяет и возвращает номер, тип которого указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращённое значение не равно null, но может быть пустым в случае ошибки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<INumberObject> AcquireNumberByTypeAsync(
    	this INumberComposer composer,
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AcquireNumberByTypeAsync ( 
    	composer As INumberComposer,
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of INumberObject)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<INumberObject^>^ AcquireNumberByTypeAsync(
    	INumberComposer^ composer, 
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AcquireNumberByTypeAsync : 
            composer : INumberComposer * 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<INumberObject> 
#### Параметры
composer [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)
    Объект, обрабатывающий логику выделения и изменения номеров карточки.
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером, в котором указывается тип номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Выделенный номер. Не равен null, но может быть пустым в случае ошибки.
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
