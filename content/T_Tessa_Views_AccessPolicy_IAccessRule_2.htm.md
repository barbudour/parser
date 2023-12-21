# IAccessRule<TAccessSubject, TMandatoryContext> \- интерфейс
Описание интерфейса правила доступа
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAccessRule<in TAccessSubject, in TMandatoryContext>
VB __Копировать
     Public Interface IAccessRule(Of In TAccessSubject, In TMandatoryContext)
C++ __Копировать
    generic<typename TAccessSubject, typename TMandatoryContext>
    public interface class IAccessRule
F# __Копировать
     type IAccessRule<'TAccessSubject, 'TMandatoryContext> = interface end
#### Параметры типа
TAccessSubject
     Тип элемента 
TMandatoryContext
     Тип контекста 
## __Методы
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_IAccessRule_2_IsSatisfiedByAsync.htm)|
Выполняет проверку доступности объекта subject  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
