# IExtensionPolicyContainer.IsRegistered<TPolicy> \- метод
Возвращает признак того, что политика для заданного типа была зарегистрирована
в контейнере.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsRegistered<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Function IsRegistered(Of TPolicy As {Class, IExtensionPolicy}) As Boolean
C++ __Копировать
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    bool IsRegistered()
F# __Копировать
     abstract IsRegistered : unit -> bool  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемой политики.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если политика для заданного типа была зарегистрирована в контейнере;
false в противном случае.
## __См. также
#### Ссылки
[IExtensionPolicyContainer -
](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
