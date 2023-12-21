# RegisterPoliciesStrategy - конструктор
Создаёт экземпляр класса с указанием делегата, выполняющего конфигурирование
политик для всех расширений в процессе применения текущей стратегии.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public RegisterPoliciesStrategy(
    	ExtensionPolicyConfigurator policyConfigurator
    )
VB __Копировать
     Public Sub New ( 
    	policyConfigurator As ExtensionPolicyConfigurator
    )
C++ __Копировать
     public:
    RegisterPoliciesStrategy(
    	ExtensionPolicyConfigurator^ policyConfigurator
    )
F# __Копировать
     new : 
            policyConfigurator : ExtensionPolicyConfigurator -> RegisterPoliciesStrategy
#### Параметры
policyConfigurator
[ExtensionPolicyConfigurator](T_Tessa_Extensions_ExtensionPolicyConfigurator.htm)
     Делегат, выполняющий конфигурирование политик для всех расширений, или null, если конфигурирование не требуется. 
## __См. также
#### Ссылки
[RegisterPoliciesStrategy - ](T_Tessa_Extensions_RegisterPoliciesStrategy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
