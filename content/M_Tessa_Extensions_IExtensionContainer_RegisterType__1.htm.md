# IExtensionContainer.RegisterType<TExtension> \- метод
Регистрирует тип расширения в контейнере. Существующая регистрация замещается.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IExtensionContainer RegisterType<TExtension>(
    	ExtensionTypeConfigurator<TExtension> typeConfigurator,
    	ExtensionPolicyConfigurator policyConfigurator = null
    )
    where TExtension : class, IExtension
VB __Копировать
     Function RegisterType(Of TExtension As {Class, IExtension}) ( 
    	typeConfigurator As ExtensionTypeConfigurator(Of TExtension),
    	Optional policyConfigurator As ExtensionPolicyConfigurator = Nothing
    ) As IExtensionContainer
C++ __Копировать
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    IExtensionContainer^ RegisterType(
    	ExtensionTypeConfigurator<TExtension>^ typeConfigurator, 
    	ExtensionPolicyConfigurator^ policyConfigurator = nullptr
    )
F# __Копировать
     abstract RegisterType : 
            typeConfigurator : ExtensionTypeConfigurator<'TExtension> * 
            ?policyConfigurator : ExtensionPolicyConfigurator 
    (* Defaults:
            let _policyConfigurator = defaultArg policyConfigurator null
    *)
    -> IExtensionContainer  when 'TExtension : not struct and IExtension
#### Параметры
typeConfigurator
[ExtensionTypeConfigurator](T_Tessa_Extensions_ExtensionTypeConfigurator_1.htm)<TExtension>
    Делегат, выполняющий регистрацию типа расширения в контейнере.
policyConfigurator
[ExtensionPolicyConfigurator](T_Tessa_Extensions_ExtensionPolicyConfigurator.htm)
(Optional)
     Делегат, выполняющий конфигурирование политик, относящихся к типу расширения, или null, если конфигурирование политик не требуется. 
#### Параметры типа
TExtension
    Тип регистрируемого расширения.
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Контейнер для цепочки вызовов.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр typeConfigurator равен null.  
---|---  
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Невозможно зарегистрировать тип расширения
[IExtension](T_Tessa_Extensions_IExtension.htm). Укажите наследник типа.  
## __См. также
#### Ссылки
[IExtensionContainer - ](T_Tessa_Extensions_IExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
