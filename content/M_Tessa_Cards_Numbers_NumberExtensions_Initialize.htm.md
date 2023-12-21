# NumberExtensions.Initialize - метод
Выполняет инициализацию свойств для контекста действий с номером, если они не
были инициализированы:
[Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm),
[Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm) и
[EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm). Инициализация
вызывается автоматически для вызова расширяемых методов
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberContextInitializationFlags Initialize(
    	this INumberContext context,
    	INumberDirectorBase director,
    	NumberEventType eventType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function Initialize ( 
    	context As INumberContext,
    	director As INumberDirectorBase,
    	eventType As NumberEventType
    ) As NumberContextInitializationFlags
C++ __Копировать
     public:
    [ExtensionAttribute]
    static NumberContextInitializationFlags Initialize(
    	INumberContext^ context, 
    	INumberDirectorBase^ director, 
    	NumberEventType^ eventType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member Initialize : 
            context : INumberContext * 
            director : INumberDirectorBase * 
            eventType : NumberEventType -> NumberContextInitializationFlags 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
director [INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm)
    Объект, реализующий произвольное взаимодействие с номерами карточек.
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
    Тип события, происходящего с номером.
#### Возвращаемое значение
[NumberContextInitializationFlags](T_Tessa_Cards_Numbers_NumberContextInitializationFlags.htm)  
Флаги, определяющие результат инициализации контекста события, происходящего с
номером.
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
