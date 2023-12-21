# ExtensionPolicyConfigurator - делегат
Делегат, выполняющий конфигурирование политик в заданном контейнере.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IExtensionPolicyContainer ExtensionPolicyConfigurator(
    	IExtensionPolicyContainer policies
    )
VB __Копировать
     Public Delegate Function ExtensionPolicyConfigurator ( 
    	policies As IExtensionPolicyContainer
    ) As IExtensionPolicyContainer
C++ __Копировать
     public delegate IExtensionPolicyContainer^ ExtensionPolicyConfigurator(
    	IExtensionPolicyContainer^ policies
    )
F# __Копировать
     type ExtensionPolicyConfigurator = 
        delegate of 
            policies : IExtensionPolicyContainer -> IExtensionPolicyContainer
#### Параметры
policies
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер, в котором выполняется конфигурирование политик.
#### Возвращаемое значение
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)  
Контейнер policies для цепочки вызовов.
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
