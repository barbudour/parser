# IViewWalker<TContext> \- интерфейс
Описание интерфейса для объектов реализующих фильтрацию списка представлений
согласно политики доступности
[IViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewWalker<TContext>
VB __Копировать
     Public Interface IViewWalker(Of TContext)
C++ __Копировать
    generic<typename TContext>
    public interface class IViewWalker
F# __Копировать
     type IViewWalker<'TContext> = interface end
#### Параметры типа
TContext
     Тип контекста 
## __Методы
[ApplyAsync(IEnumerable<ITessaView>, TContext,
CancellationToken)](M_Tessa_Views_AccessPolicy_IViewWalker_1_ApplyAsync.htm)|
Осуществляет фильтрацию списка представлений views согласно политике
доступности
[IViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)
в контексте context  
---|---  
[ApplyAsync(IEnumerable<ITessaView>, TContext, AccessRuleExecutor<ITessaView,
TContext>,
CancellationToken)](M_Tessa_Views_AccessPolicy_IViewWalker_1_ApplyAsync_1.htm)|
Осуществляет фильтрацию списка представлений views согласно политике
доступности
[IViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)
в контексте context с помощью исполнителя правил ruleExecutor  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
