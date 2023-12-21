# DefaultConfigurationVersionDeleteExtension - класс
Увеличивает версию конфигурации при удалении карточек, связанных с типовым
решением. Также проверяет, что конфигурация не находится в режиме защиты от
изменений [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm). Должно
быть зарегистрировано для только определённых карточек .WhenCardTypes(...), а
также для всех видов удаления карточки .WhenAnyDeleteMethod().
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DefaultConfigurationVersionDeleteExtension : CardDeleteExtension
VB __Копировать
     Public NotInheritable Class DefaultConfigurationVersionDeleteExtension
    	Inherits CardDeleteExtension
C++ __Копировать
     public ref class DefaultConfigurationVersionDeleteExtension sealed : public CardDeleteExtension
F# __Копировать
     [<SealedAttribute>]
    type DefaultConfigurationVersionDeleteExtension = 
        class
            inherit CardDeleteExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm) __ DefaultConfigurationVersionDeleteExtension
##  __Конструкторы
[DefaultConfigurationVersionDeleteExtension](M_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionDeleteExtension__ctor.htm)|
Инициализирует новый экземпляр класса
DefaultConfigurationVersionDeleteExtension  
---|---  
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Унаследован от
[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterRequest.htm)|
Действие, выполняемое после удаления карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm))  
[AfterRequestFinally](M_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionDeleteExtension_AfterRequestFinally.htm)|  
(Переопределяет
[CardDeleteExtension.AfterRequestFinally(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterRequestFinally.htm))  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_CardDeleteExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
(Унаследован от
[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm))  
[BeforeRequest](M_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionDeleteExtension_BeforeRequest.htm)|  
(Переопределяет
[CardDeleteExtension.BeforeRequest(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_CardDeleteExtension_BeforeRequest.htm))  
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
[Tessa.Extensions.Default.Server.Cards - пространство
имён](N_Tessa_Extensions_Default_Server_Cards.htm)
