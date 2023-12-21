# ExtensionPolicyContainer.IsRegistered<TPolicy> \- метод
Возвращает признак того, что политика для заданного типа была зарегистрирована
в контейнере.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsRegistered<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Public Function IsRegistered(Of TPolicy As {Class, IExtensionPolicy}) As Boolean
C++ __Копировать
     public:
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    virtual bool IsRegistered() sealed
F# __Копировать
     abstract IsRegistered : unit -> bool  when 'TPolicy : not struct and IExtensionPolicy
    override IsRegistered : unit -> bool  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемой политики.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если политика для заданного типа была зарегистрирована в контейнере;
false в противном случае.
#### Реализации
[IExtensionPolicyContainer.IsRegistered<TPolicy>()](M_Tessa_Extensions_IExtensionPolicyContainer_IsRegistered__1.htm)  
##  __См. также
#### Ссылки
[ExtensionPolicyContainer - ](T_Tessa_Extensions_ExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
