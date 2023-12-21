# IViewAccessRule<TContext> \- интерфейс
Описание интерфейса правила доступности для представления
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewAccessRule<in TContext> : IAccessRule<ITessaView, TContext>
VB __Копировать
     Public Interface IViewAccessRule(Of In TContext)
    	Inherits IAccessRule(Of ITessaView, TContext)
C++ __Копировать
    generic<typename TContext>
    public interface class IViewAccessRule : IAccessRule<ITessaView^, TContext>
F# __Копировать
     type IViewAccessRule<'TContext> = 
        interface
            interface IAccessRule<ITessaView, 'TContext>
        end
Implements
    [IAccessRule](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm)<[ITessaView](T_Tessa_Views_ITessaView.htm), TContext>
#### Параметры типа
TContext
     Тип контекста 
## __Методы
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_IAccessRule_2_IsSatisfiedByAsync.htm)|
Выполняет проверку доступности объекта subject  
(Унаследован от [IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
