# IDocLoadExtensionContext - интерфейс
Контекст расширений для потокового ввода.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IDocLoadExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IDocLoadExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IDocLoadExtensionContext : IExtensionContext
F# __Копировать
     type IDocLoadExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[Barcode](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_Barcode.htm)|
Штрих-код, распознанный на изображении.  
---|---  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[CardID](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_CardID.htm)|
Идентификатор карточки, найденный расширением по штрих-коду, указанному в
контексте. Расширение должно установить идентификатор в этом свойстве.  
[DbScope](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_DbScope.htm)|
Объект для взаимодействия с базой данных.  
[Document](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_Document.htm)|
Документ, прикрепляемый к карточке.  
[InputFilePath](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_InputFilePath.htm)|
Файл, полученный на распознавание.  
[Settings](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_Settings.htm)|
Настройки модуля потокового сканирования.  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
