# IExtraViewProvider - интерфейс
Интерфейс, предоставляющий доступ к объекту программного представления с
собственной метаинформацией и логикой выполнения.
Классы, реализующие интерфейс, должны быть зарегистрированы в Unity по разным
именам: UnityContainer.RegisterType<IExtraViewProvider,
MyComputedViewProvider>(nameof(MyComputedViewProvider), new
ContainerControlledLifetimeManager());
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IExtraViewProvider
VB __Копировать
     Public Interface IExtraViewProvider
C++ __Копировать
     public interface class IExtraViewProvider
F# __Копировать
     type IExtraViewProvider = interface end
##  __Методы
[GetExtraView](M_Tessa_Views_IExtraViewProvider_GetExtraView.htm)|  Возвращает
программное представление.  
---|---  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
