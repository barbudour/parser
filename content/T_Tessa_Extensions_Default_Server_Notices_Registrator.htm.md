# Registrator - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Notices](N_Tessa_Extensions_Default_Server_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [RegistratorAttribute(ExtensionStage.AfterPlatform)]
    public sealed class Registrator : RegistratorBase
VB __Копировать
    <RegistratorAttribute(ExtensionStage.AfterPlatform)>
    Public NotInheritable Class Registrator
    	Inherits RegistratorBase
C++ __Копировать
    [RegistratorAttribute(ExtensionStage::AfterPlatform)]
    public ref class Registrator sealed : public RegistratorBase
F# __Копировать
     [<SealedAttribute>]
    [<RegistratorAttribute(ExtensionStage.AfterPlatform)>]
    type Registrator = 
        class
            inherit RegistratorBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm) __ Registrator
##  __Конструкторы
[Registrator](M_Tessa_Extensions_Default_Server_Notices_Registrator__ctor.htm)|
Инициализирует новый экземпляр класса Registrator  
---|---  
##  __Свойства
[InstanceName](P_Tessa_Extensions_RegistratorBase_InstanceName.htm)|  Имя
экземпляра сервера или null, если регистрация выполняется на клиенте.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
---|---  
[IsPlatform](P_Tessa_Extensions_RegistratorBase_IsPlatform.htm)|  Признак
того, что объект выполняет регистрацию платформенных расширений. Этот признак
используется системой, не рекомендуется его устанавливать.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
[IsSealed](P_Tessa_Extensions_RegistratorBase_IsSealed.htm)| Признак того, что
объект был защищён от изменений.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
[SessionType](P_Tessa_Extensions_RegistratorBase_SessionType.htm)| Тип сессии.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
[Tag](P_Tessa_Extensions_RegistratorBase_Tag.htm)|  Флаговое перечисление с
тегами регистратора, которые ограничивают область его использования. По
умолчанию используются теги [Tessa.Extensions.RegistratorTag.Default].  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
[UnityContainer](P_Tessa_Extensions_RegistratorBase_UnityContainer.htm)|
Контейнер Unity, в котором выполняется регистрация. Гарантированно не равен
null.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
##  __Методы
[CheckSealed](M_Tessa_Extensions_RegistratorBase_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
---|---  
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
[FinalizeRegistration](M_Tessa_Extensions_RegistratorBase_FinalizeRegistration.htm)|
Завершает регистрацию. В этом методе рекомендуется получить зависимости из
Unity и выполнить их настройку.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
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
[InitializeExtensions](M_Tessa_Extensions_RegistratorBase_InitializeExtensions.htm)|
Выполняет инициализацию заданного контейнера расширений. Рекомендуется не
выполнять регистрацию Unity в этом объекте.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
[InitializeRegistration](M_Tessa_Extensions_RegistratorBase_InitializeRegistration.htm)|
Инициализирует регистрацию. В этом методе рекомендуется зарегистрировать
зависимости в Unity, которые необходимы уже на момент регистрации расширений.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterExtensions](M_Tessa_Extensions_Default_Server_Notices_Registrator_RegisterExtensions.htm)|  
(Переопределяет
[RegistratorBase.RegisterExtensions(IExtensionContainer)](M_Tessa_Extensions_RegistratorBase_RegisterExtensions.htm))  
[RegisterUnity](M_Tessa_Extensions_Default_Server_Notices_Registrator_RegisterUnity.htm)|  
(Переопределяет
[RegistratorBase.RegisterUnity()](M_Tessa_Extensions_RegistratorBase_RegisterUnity.htm))  
[Seal](M_Tessa_Extensions_RegistratorBase_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от [RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm))  
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
[Tessa.Extensions.Default.Server.Notices - пространство
имён](N_Tessa_Extensions_Default_Server_Notices.htm)
