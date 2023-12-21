# IKrCompilationCache - интерфейс
Кэш с результатами компиляции объектов подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrCompilationCache
VB __Копировать
     Public Interface IKrCompilationCache
C++ __Копировать
     public interface class IKrCompilationCache
F# __Копировать
     type IKrCompilationCache = interface end
##  __Методы
[BuildAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationCache_BuildAsync.htm)|
Выполняет сборку, если в кэше нет сборки или сборка invalidate. Если в кэше
есть актуальная сборка, возвращается null.  
---|---  
[GetAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationCache_GetAsync.htm)|
Возвращает значения из кэша.  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationCache_InvalidateAsync.htm)|
Сбрасывает значения кэша.  
[RebuildAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationCache_RebuildAsync.htm)|
Явно сбрасывает кэш сборки и выполняет пересборку. Кэш KrStageTenolateCache не
сбрасывается.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
