# IKrVirtualFileScriptContext - интерфейс
Контекст выполнени скриптов для виртуальных файлов в
[IKrVirtualFileScript](T_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScript.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Files.VirtualFiles.Compilation](N_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrVirtualFileScriptContext : IExtensionContext
VB __Копировать
     Public Interface IKrVirtualFileScriptContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrVirtualFileScriptContext : IExtensionContext
F# __Копировать
     type IKrVirtualFileScriptContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Card](P_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScriptContext_Card.htm)|
Объект карточки, к которой относится виртуальный файл  
[CardFile](P_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScriptContext_CardFile.htm)|
Общая информация о файла, прикреплённом к карточке  
[Container](P_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScriptContext_Container.htm)|
Контейнер зависимостей  
[DbScope](P_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScriptContext_DbScope.htm)|
Объект для доступа к базе данных  
[File](P_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScriptContext_File.htm)|
Объект файла  
[Session](P_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation_IKrVirtualFileScriptContext_Session.htm)|
Текущая сессия  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Files.VirtualFiles.Compilation - пространство
имён](N_Tessa_Extensions_Default_Server_Files_VirtualFiles_Compilation.htm)
