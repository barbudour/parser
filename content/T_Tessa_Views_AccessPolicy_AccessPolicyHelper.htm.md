# AccessPolicyHelper - класс
Вспомогательные методы для работы с политиками доступности
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class AccessPolicyHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class AccessPolicyHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class AccessPolicyHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type AccessPolicyHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AccessPolicyHelper
##  __Методы
[RegisterOpenedRuleType](M_Tessa_Views_AccessPolicy_AccessPolicyHelper_RegisterOpenedRuleType.htm)|
Регистрирует в контейнере приложения container тип правила type. Тип должен
быть открытым обобщенным типов реализующим интерфейс
[IAccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm)  
---|---  
[RegisterRuleType(IUnityContainer, Type,
Type)](M_Tessa_Views_AccessPolicy_AccessPolicyHelper_RegisterRuleType.htm)|
Осуществляет регистрацию в контейнере приложения правила  
[RegisterRuleType<TInterface,
TImplementation>(IUnityContainer)](M_Tessa_Views_AccessPolicy_AccessPolicyHelper_RegisterRuleType__2.htm)|
Регистрирует правило в контейнере container  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
