# CardMetadataExtensionContext - класс
Контекст расширения, выполняемого при построении метаинформации по типам
карточек [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardMetadataExtensionContext : ICardMetadataExtensionContext, 
    	ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public NotInheritable Class CardMetadataExtensionContext
    	Implements ICardMetadataExtensionContext, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public ref class CardMetadataExtensionContext sealed : ICardMetadataExtensionContext, 
    	ITraceableExtensionContext, IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type CardMetadataExtensionContext = 
        class
            interface ICardMetadataExtensionContext
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataExtensionContext
Implements
    [ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Конструкторы
[CardMetadataExtensionContext](M_Tessa_Cards_Extensions_CardMetadataExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_CardMetadata.htm)|
Построенная метаинформация по типам карточек, которую расширение может
изменять, или null, если расширение вызвано на этапе, на котором
метаинформация ещё не построена.  
[CardTypes](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_CardTypes.htm)|
Типы карточек, используемые для построения метаинформации.  
[DelayedSchemeCheckCardTypeIDSet](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_DelayedSchemeCheckCardTypeIDSet.htm)|
Идентификаторы типов карточек, проверка схемы для которых выполняется после
выполнения всех расширений на метаинформацию.
Рекомендуется добавить идентификатор типа карточки в методе расширения
[ModifyTypes(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyTypes.htm),
чтобы позже в методе расширения
[ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm)
добавить секции и колонки, отсутствующие в схеме данных.
Если по завершении этого метода в типе карточки cardType.SchemeItems
присутствуют ссылки на секции или колонки, отсутствующие в секциях
cardMetadata.GetSectionsAsync(), то тип считается повреждённым, и добавляется
такое же сообщение об ошибке, как если бы проверка типа не была отложена.  
[EnableTracing](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[GlobalReferences](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_GlobalReferences.htm)|
Словарь, содержащий глобальные объекты
([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)), совместно
использующиеся в типах карточек.  
[Info](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_Info.htm)|
Информация, используемая для передачи между расширениями в цепочке.  
[SchemeService](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_SchemeService.htm)|
Объект, обеспечивающий доступ к схеме данных.  
[ValidationResult](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
