# FileConverterCacheStoreExtension - класс
Расширение учитывает наличие в запросе ключа
[OldestPreviewRequestTimeKey](F_Tessa_FileConverters_FileConverterHelper_OldestPreviewRequestTimeKey.htm),
по которому должна быть выполнена очистка кэша. Тип карточки административный,
поэтому доступ к очистке кэша могут иметь только администраторы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileConverterCacheStoreExtension : CardStoreExtension
VB __Копировать
     Public NotInheritable Class FileConverterCacheStoreExtension
    	Inherits CardStoreExtension
C++ __Копировать
     public ref class FileConverterCacheStoreExtension sealed : public CardStoreExtension
F# __Копировать
     [<SealedAttribute>]
    type FileConverterCacheStoreExtension = 
        class
            inherit CardStoreExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __ FileConverterCacheStoreExtension
##  __Конструкторы
[FileConverterCacheStoreExtension](M_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheStoreExtension__ctor.htm)|
Инициализирует новый экземпляр класса FileConverterCacheStoreExtension  
---|---  
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BeforeCommitTransaction](M_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheStoreExtension_BeforeCommitTransaction.htm)|  
(Переопределяет
[CardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeCommitTransaction.htm))  
[BeforeRequest](M_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheStoreExtension_BeforeRequest.htm)|  
(Переопределяет
[CardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
