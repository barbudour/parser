# IAccessPolicy<TAccessSubject, TContext> \- интерфейс
Описание интерфейса проверки доступности элементов типа TAccessSubject в
соответствии с правилами текущей политики доступности элементов.
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAccessPolicy<TAccessSubject, TContext>
VB __Копировать
     Public Interface IAccessPolicy(Of TAccessSubject, TContext)
C++ __Копировать
    generic<typename TAccessSubject, typename TContext>
    public interface class IAccessPolicy
F# __Копировать
     type IAccessPolicy<'TAccessSubject, 'TContext> = interface end
#### Параметры типа
TAccessSubject
     Тип элемента 
TContext
     Тип контекста 
## __Методы
[AddRules](M_Tessa_Views_AccessPolicy_IAccessPolicy_2_AddRules.htm)|
Добавляет правила в политику безопасности  
---|---  
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_IAccessPolicy_2_IsSatisfiedByAsync.htm)|
Осуществляет проверку доступности элемента subject в соответствии с правилами
политик доступа.  
## __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
