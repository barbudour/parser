# IApplicationResourceRegistrator - интерфейс
Объект, выполняющий регистрацию словарей ресурсов .xaml в приложении
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application).
## __Definition
 **Пространство имён:** [Tessa.UI.Runtime](N_Tessa_UI_Runtime.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationResourceRegistrator
VB __Копировать
     Public Interface IApplicationResourceRegistrator
C++ __Копировать
     public interface class IApplicationResourceRegistrator
F# __Копировать
     type IApplicationResourceRegistrator = interface end
##  __Методы
[AddResourcesTo](M_Tessa_UI_Runtime_IApplicationResourceRegistrator_AddResourcesTo.htm)|
Добавляет зарегистрированные словари ресурсов в заданную коллекцию ресурсов.
Если коллекция уже содержит некоторые словари ресурсов с таким же
местоположением, то метод не добавляет словари повторно.  
---|---  
[Register(Uri)](M_Tessa_UI_Runtime_IApplicationResourceRegistrator_Register_1.htm)|
Выполняет регистрацию словаря ресурсов, доступного по заданному Uri. Если
словарь уже зарегистрирован, то не выполняет действий.  
[Register(String,
Assembly)](M_Tessa_UI_Runtime_IApplicationResourceRegistrator_Register.htm)|
Выполняет регистрацию словаря ресурсов, доступного по заданному относительному
пути для указанной сборки. Если словарь уже зарегистрирован, то не выполняет
действий.  
## __Методы расширения
[AddResourcesTo](M_Tessa_UI_Runtime_UIRuntimeExtensions_AddResourcesTo.htm)|
Добавляет зарегистрированные словари ресурсов в заданное приложение. Если
приложение содержит некоторые словари ресурсов с таким же местоположением, то
метод не добавляет словари повторно.  
(Определяется
[UIRuntimeExtensions](T_Tessa_UI_Runtime_UIRuntimeExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Runtime - пространство имён](N_Tessa_UI_Runtime.htm)
