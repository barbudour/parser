# IExtensionContainer.RegisterExtension<TExtension, TConcreteExtension> \-
метод
Регистрирует конкретное расширение в контейнере. Существующая регистрация
замещается.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IExtensionContainer RegisterExtension<TExtension, TConcreteExtension>(
    	ExtensionPolicyConfigurator policyConfigurator = null
    )
    where TExtension : class, IExtension
    where TConcreteExtension : TExtension
VB __Копировать
     Function RegisterExtension(Of TExtension As {Class, IExtension}, TConcreteExtension As TExtension) ( 
    	Optional policyConfigurator As ExtensionPolicyConfigurator = Nothing
    ) As IExtensionContainer
C++ __Копировать
    generic<typename TExtension, typename TConcreteExtension>
    where TExtension : ref class, IExtension
    where TConcreteExtension : TExtension
    IExtensionContainer^ RegisterExtension(
    	ExtensionPolicyConfigurator^ policyConfigurator = nullptr
    )
F# __Копировать
     abstract RegisterExtension : 
            ?policyConfigurator : ExtensionPolicyConfigurator 
    (* Defaults:
            let _policyConfigurator = defaultArg policyConfigurator null
    *)
    -> IExtensionContainer  when 'TExtension : not struct and IExtension when 'TConcreteExtension : 'TExtension
#### Параметры
policyConfigurator
[ExtensionPolicyConfigurator](T_Tessa_Extensions_ExtensionPolicyConfigurator.htm)
(Optional)
     Делегат, выполняющий конфигурирование политик, относящихся к конкретному расширению, или null, если конфигурирование политик не требуется. 
#### Параметры типа
TExtension
    Тип расширения, подклассом которого является конкретное расширение.
TConcreteExtension
    Тип конкретного расширения, регистрируемого в контейнере.
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Контейнер для цепочки вызовов.
##  __Исключения
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Невозможно зарегистрировать расширение, тип которого TExtension совпадает с
базовым типом TConcreteExtension. Укажите наследник типа.  
---|---  
## __См. также
#### Ссылки
[IExtensionContainer - ](T_Tessa_Extensions_IExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
