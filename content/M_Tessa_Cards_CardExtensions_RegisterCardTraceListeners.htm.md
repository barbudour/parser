# CardExtensions.RegisterCardTraceListeners - метод
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений карточек, и записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с карточками, поэтому рекомендуется не
выполнять такую регистрацию в среде, с которой работают конечные пользователи.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionContainer RegisterCardTraceListeners(
    	this IExtensionContainer container,
    	ExtensionTraceListenerType listenerType,
    	long? minConsiderableMilliseconds
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterCardTraceListeners ( 
    	container As IExtensionContainer,
    	listenerType As ExtensionTraceListenerType,
    	minConsiderableMilliseconds As Long?
    ) As IExtensionContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionContainer^ RegisterCardTraceListeners(
    	IExtensionContainer^ container, 
    	ExtensionTraceListenerType listenerType, 
    	Nullable<long long> minConsiderableMilliseconds
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterCardTraceListeners : 
            container : IExtensionContainer * 
            listenerType : ExtensionTraceListenerType * 
            minConsiderableMilliseconds : Nullable<int64> -> IExtensionContainer 
#### Параметры
container [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер, в котором регистрируются объекты.
listenerType
[ExtensionTraceListenerType](T_Tessa_Extensions_ExtensionTraceListenerType.htm)
    Тип объекта, определяющий способ отслеживания событий.
minConsiderableMilliseconds
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
     Минимальное количество миллисекунд, которое должно выполняться расширение для того, чтобы для него было создано сообщение трассировки, если используются трассировщики [ServerProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm) или [ClientProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm). Если значение равно 0 или отрицательное, то сообщения трассировки создаются для всех объектов. Если значение равно null, то время выполнения расширения замеряется с интервалом по умолчанию [DefaultProfileMinConsiderableMilliseconds](F_Tessa_Extensions_DefaultExtensionTraceListener_DefaultProfileMinConsiderableMilliseconds.htm). 
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Заданный контейнер container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
