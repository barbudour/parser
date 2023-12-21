# NotificationCardsStrictSecurity - класс
Объект для установки и проверки доступа к карточке "Уведомление" при наличии
ограничений в конфигурации.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NotificationCardsStrictSecurity : CardStrictSecurity
VB __Копировать
     Public NotInheritable Class NotificationCardsStrictSecurity
    	Inherits CardStrictSecurity
C++ __Копировать
     public ref class NotificationCardsStrictSecurity sealed : public CardStrictSecurity
F# __Копировать
     [<SealedAttribute>]
    type NotificationCardsStrictSecurity = 
        class
            inherit CardStrictSecurity
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm) __ NotificationCardsStrictSecurity
##  __Конструкторы
[NotificationCardsStrictSecurity](M_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity__ctor.htm)|
Инициализирует новый экземпляр класса NotificationCardsStrictSecurity  
---|---  
##  __Методы
[CheckOnDeleteAsync](M_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity_CheckOnDeleteAsync.htm)|
Проверяет доступ к карточке при её удалении с ограничением flag.  
(Переопределяет
[CardStrictSecurity.CheckOnDeleteAsync(ICardDeleteExtensionContext,
ConfigurationFlags)](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_CheckOnDeleteAsync.htm))  
---|---  
[CheckOnNewAsync](M_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity_CheckOnNewAsync.htm)|
Проверяет доступ к карточке при её создании с ограничением flag.  
(Переопределяет [CardStrictSecurity.CheckOnNewAsync(ICardNewExtensionContext,
ConfigurationFlags)](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_CheckOnNewAsync.htm))  
[CheckOnStoreAsync](M_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity_CheckOnStoreAsync.htm)|
Проверяет доступ к карточке при её сохранении с ограничением flag.  
(Переопределяет
[CardStrictSecurity.CheckOnStoreAsync(ICardStoreExtensionContext,
ConfigurationFlags)](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_CheckOnStoreAsync.htm))  
[CheckSealedAsync](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_CheckSealedAsync.htm)|
Проверяет доступ к карточке при наличии ограничения
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)  
(Унаследован от
[CardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm))  
[CheckStrictSecurityAsync](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_CheckStrictSecurityAsync.htm)|
Проверяет доступ к карточке при наличии ограничения
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)  
(Унаследован от
[CardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm))  
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
[UpdateOnSealedAsync](M_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity_UpdateOnSealedAsync.htm)|
Обновляет доступ к карточке при наличии ограничения
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)  
(Переопределяет [CardStrictSecurity.UpdateOnSealedAsync(Card,
CancellationToken)](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_UpdateOnSealedAsync.htm))  
[UpdateOnStrictSecurityAsync](M_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity_UpdateOnStrictSecurityAsync.htm)|
Обновляет доступ к карточке при наличии ограничения
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)  
(Переопределяет [CardStrictSecurity.UpdateOnStrictSecurityAsync(Card,
CancellationToken)](M_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity_UpdateOnStrictSecurityAsync.htm))  
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
