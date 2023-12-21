# IKrCompiler - интерфейс
Объект, выполняющий компиляцию объектов подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrCompiler
VB __Копировать
     Public Interface IKrCompiler
C++ __Копировать
     public interface class IKrCompiler
F# __Копировать
     type IKrCompiler = interface end
##  __Свойства
[DefaultIgnoreWarnings](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompiler_DefaultIgnoreWarnings.htm)|
Возвращает список стандартных игнорируемых предупреждений.  
---|---  
[DefaultReferences](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompiler_DefaultReferences.htm)|
Список стандартных зависимостей, используемых при компиляции. Доступно для
изменения, но не потокобезопасно.  
[DefaultUsings](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompiler_DefaultUsings.htm)|
Список стандартных пространств имен, подставляемых в каждую единицу
компиляции. Доступно для изменения, но не потокобезопасно.  
## __Методы
[Compile](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompiler_Compile.htm)|
Выполнить компиляцию на основе контекста. В контексте должны быть указаны
шаблоны этапов, базовые методы, пространства имен и референсы.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
