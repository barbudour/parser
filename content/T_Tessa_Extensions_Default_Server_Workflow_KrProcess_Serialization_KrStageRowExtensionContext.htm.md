# KrStageRowExtensionContext - класс
Контекст расширения на сериализацию этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageRowExtensionContext : IKrStageRowExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrStageRowExtensionContext
    	Implements IKrStageRowExtensionContext, IExtensionContext
C++ __Копировать
     public ref class KrStageRowExtensionContext sealed : IKrStageRowExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrStageRowExtensionContext = 
        class
            interface IKrStageRowExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrStageRowExtensionContext
Implements
    [IKrStageRowExtensionContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrStageRowExtensionContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext__ctor.htm)|
Инициализирует новый экземпляр класса KrStageRowExtensionContext.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_CancellationToken.htm)|  
---|---  
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_CardContext.htm)|
Внешний контекст расширения. Может быть null.  
[CardToRepair](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_CardToRepair.htm)|
Карточка с настройками этапа, используемая для восстановления при загрузке.
Имеет значение null перед началом сериализации настроек этапов:
[BeforeSerialization(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm).  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_CardType.htm)|
Тип карточки. Перед сериализацией настроек этапов
([BeforeSerialization(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm))
возвращает тип
[InnerCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_InnerCard.htm),
после десериализации настроек этапов возвращает тип
[OuterCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_OuterCard.htm).  
[InnerCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_InnerCard.htm)|
"Входная" карточка.  
[OuterCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_OuterCard.htm)|
"Выходная" карточка.  
[RouteCardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_RouteCardType.htm)|
Тип карточки маршрута. Перед сериализацией настроек этапов
([BeforeSerialization(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm))
тип innerCard, после десериализации настроек этапов тип outerCard.  
[StageStorages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensionContext_StageStorages.htm)|
Коллекция ключ-значение, где ключ - идентификатор строки этапа, значение -
коллекция ключ-значение содержащая параметры этапа. Имеет значение null после
десериализации параметров этапов:
[DeserializationBeforeRepair(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_DeserializationBeforeRepair.htm)
и
[DeserializationAfterRepair(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_DeserializationAfterRepair.htm).  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)
