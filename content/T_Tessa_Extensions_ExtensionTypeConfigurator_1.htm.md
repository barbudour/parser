# ExtensionTypeConfigurator<TExtension> \- делегат
Делегат, выполняющий регистрацию типа расширения в контейнере.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IExtensionTypeRegistrator<TExtension> ExtensionTypeConfigurator<TExtension>(
    	IExtensionTypeRegistrator<TExtension> registrator
    )
    where TExtension : class, IExtension
VB __Копировать
     Public Delegate Function ExtensionTypeConfigurator(Of TExtension As {Class, IExtension}) ( 
    	registrator As IExtensionTypeRegistrator(Of TExtension)
    ) As IExtensionTypeRegistrator(Of TExtension)
C++ __Копировать
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    public delegate IExtensionTypeRegistrator<TExtension>^ ExtensionTypeConfigurator(
    	IExtensionTypeRegistrator<TExtension>^ registrator
    )
F# __Копировать
     type ExtensionTypeConfigurator = 
        delegate of 
            registrator : IExtensionTypeRegistrator<'TExtension> -> IExtensionTypeRegistrator<'TExtension>
#### Параметры
registrator
[IExtensionTypeRegistrator](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm)<TExtension>
    Объект, выполняющий регистрацию типа расширения в контейнере.
#### Параметры типа
TExtension
    Тип регистрируемого расширения.
#### Возвращаемое значение
[IExtensionTypeRegistrator](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm)<TExtension>  
Объект registrator для цепочки вызовов.
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
