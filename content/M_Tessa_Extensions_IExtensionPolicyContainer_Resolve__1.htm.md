# IExtensionPolicyContainer.Resolve<TPolicy> \- метод
Возвращает политику заданного типа, зарегистрированную в контейнере. Если для
типа зарегистрировано несколько политик, то возвращается последняя.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     TPolicy Resolve<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Function Resolve(Of TPolicy As {Class, IExtensionPolicy}) As TPolicy
C++ __Копировать
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    TPolicy Resolve()
F# __Копировать
     abstract Resolve : unit -> 'TPolicy  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемой политики.
#### Возвращаемое значение
TPolicy  
Политика заданого типа, зарегистрированная в контейнере.
##  __См. также
#### Ссылки
[IExtensionPolicyContainer -
](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
