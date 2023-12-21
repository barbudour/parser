# ExtensionContainer.RegisterTraceListener<TExtension> \- метод
Регистрирует объект, выполняющий отслеживание событий, происходящих при
выполнении расширений заданного типа. Если для заданного типа расширения
TExtension уже был зарегистрирован такой объект, то он заменяется на указанный
объект traceListener.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IExtensionContainer RegisterTraceListener<TExtension>(
    	IExtensionTraceListener traceListener
    )
    where TExtension : class, IExtension
VB __Копировать
     Public Function RegisterTraceListener(Of TExtension As {Class, IExtension}) ( 
    	traceListener As IExtensionTraceListener
    ) As IExtensionContainer
C++ __Копировать
     public:
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    virtual IExtensionContainer^ RegisterTraceListener(
    	IExtensionTraceListener^ traceListener
    ) sealed
F# __Копировать
     abstract RegisterTraceListener : 
            traceListener : IExtensionTraceListener -> IExtensionContainer  when 'TExtension : not struct and IExtension
    override RegisterTraceListener : 
            traceListener : IExtensionTraceListener -> IExtensionContainer  when 'TExtension : not struct and IExtension
#### Параметры
traceListener
[IExtensionTraceListener](T_Tessa_Extensions_IExtensionTraceListener.htm)
    Объект, выполняющий отслеживание событий.
#### Параметры типа
TExtension
    Тип расширений, для которого регистрируется объект.
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Контейнер для цепочки вызовов.
#### Реализации
[IExtensionContainer.RegisterTraceListener<TExtension>(IExtensionTraceListener)](M_Tessa_Extensions_IExtensionContainer_RegisterTraceListener__1.htm)  
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр traceListener равен null.  
---|---  
## __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
