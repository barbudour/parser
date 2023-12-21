# IExtensionPolicyContainer.TryResolve<TPolicy> \- метод
Возвращает политику заданного типа, зарегистрированную в контейнере, или null,
если политика не была зарегистрирована. Если для типа зарегистрировано
несколько политик, то возвращается последняя.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     TPolicy TryResolve<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Function TryResolve(Of TPolicy As {Class, IExtensionPolicy}) As TPolicy
C++ __Копировать
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    TPolicy TryResolve()
F# __Копировать
     abstract TryResolve : unit -> 'TPolicy  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемой политики.
#### Возвращаемое значение
TPolicy  
Политика заданого типа, зарегистрированная в контейнере, или null, если
политика не была зарегистрирована.
## __См. также
#### Ссылки
[IExtensionPolicyContainer -
](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
