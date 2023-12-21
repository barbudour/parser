# KrCardMetadataExtensionBase - класс
Базовый класс расширений на метаинформацию типового решения. Расширяет типы
карточек KrCard, KrStageTemplate, KrSecondaryProcess. И добавляет формы,
валидаторы и расширения из KrCard во все карточки типового решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrCardMetadataExtensionBase : CardTypeMetadataExtension
VB __Копировать
     Public MustInherit Class KrCardMetadataExtensionBase
    	Inherits CardTypeMetadataExtension
C++ __Копировать
     public ref class KrCardMetadataExtensionBase abstract : public CardTypeMetadataExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type KrCardMetadataExtensionBase = 
        class
            inherit CardTypeMetadataExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm) __[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm) __ KrCardMetadataExtensionBase
Derived
[Tessa.Extensions.Default.Client.Workflow.KrProcess.KrCardMetadataExtension](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrCardMetadataExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrCardMetadataExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrCardMetadataExtension.htm)
##  __Конструкторы
[KrCardMetadataExtensionBase()](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase__ctor.htm)|
Создаёт экземпляр класса на сервере с параметрами по умолчанию.  
---|---  
[KrCardMetadataExtensionBase(ICardMetadata)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase__ctor_1.htm)|
Создаёт экземпляр класса на клиенте с указанием его зависимостей.  
## __Свойства
[ClientCardMetadata](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientCardMetadata.htm)|
Серверная метаинформация по всем типам карточек, доступная на клиенте, или
null, если выполняется построение метаинформации на сервере.  
(Унаследован от
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm))  
---|---  
[ClientMode](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientMode.htm)|
Признак того, что расширение выполняется на клиенте. Обычно это происходит при
предпросмотре типа карточки с расширениями.  
(Унаследован от
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExtendKrTypesAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase_ExtendKrTypesAsync.htm)|
Расширить и настроить указанные типы карточек.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAllSectionsAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase_GetAllSectionsAsync.htm)|
Получить все секции метаданных о таблицах.  
[GetCardTypeIDsAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase_GetCardTypeIDsAsync.htm)|
Получить идентификаторы типов карточек, входящих в типовое решение.  
[GetCardTypesOnServerAsync](M_Tessa_Cards_Extensions_CardTypeMetadataExtension_GetCardTypesOnServerAsync.htm)|
Возвращает список всех типов карточек, доступных на сервере в настоящий
момент. При вызове на сервере получает информацию из контекста context, а при
вызове на клиенте - из серверной метаинформации
[ClientCardMetadata](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientCardMetadata.htm).  
(Унаследован от
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm))  
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
[ModifyMetadata](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase_ModifyMetadata.htm)|  
(Переопределяет
[CardMetadataExtension.ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyMetadata.htm))  
[ModifyTypes](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyTypes.htm)|
Изменяет типы карточек, по которым затем будет строиться метаинформация.  
(Унаследован от
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetCardTypeAsync](M_Tessa_Cards_Extensions_CardTypeMetadataExtension_TryGetCardTypeAsync.htm)|
Возвращает метаинформацию по заданному типу карточки или null, если тип
карточки не найден.  
(Унаследован от
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm))  
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)