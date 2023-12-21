# AggregateFilterPolicy - конструктор
Создаёт экземпляр класса с указанием списка политик, последовательное
исполнение которого определяет необходимость выполнения метода расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AggregateFilterPolicy(
    	params IFilterPolicy[] filterPolicies
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray filterPolicies As IFilterPolicy()
    )
C++ __Копировать
     public:
    AggregateFilterPolicy(
    	... array<IFilterPolicy^>^ filterPolicies
    )
F# __Копировать
     new : 
            filterPolicies : IFilterPolicy[] -> AggregateFilterPolicy
#### Параметры
filterPolicies [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)[]
    Упорядоченный список политик. Значения null не допустимы.
##  __См. также
#### Ссылки
[AggregateFilterPolicy - ](T_Tessa_Extensions_AggregateFilterPolicy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
