# NumberExtensions.ExecuteNumberActionAsync - метод
Выполняет ранее установленное действие с номером по заданному ключу. Если
действие не было установлено, то возвращает false.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> ExecuteNumberActionAsync(
    	this INumberContext context,
    	string actionKey,
    	INumberObject number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ExecuteNumberActionAsync ( 
    	context As INumberContext,
    	actionKey As String,
    	number As INumberObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<bool> ExecuteNumberActionAsync(
    	INumberContext^ context, 
    	String^ actionKey, 
    	INumberObject^ number, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ExecuteNumberActionAsync : 
            context : INumberContext * 
            actionKey : string * 
            number : INumberObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
actionKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому выполняется действие с номером. Не может быть равен null. Стандартные ключи можно получить в классе [NumberContextActionKeys](T_Tessa_Cards_Numbers_NumberContextActionKeys.htm). 
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
     Номер, для которого выполняется действие. Не может быть равен null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если действие было найдено и выполнено; false, если действие не было
найдено, и поэтому не было выполнено.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm). При
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
