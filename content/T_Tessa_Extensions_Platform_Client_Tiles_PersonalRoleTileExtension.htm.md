# PersonalRoleTileExtension - класс
Расширение на модификацию тайлов для типа карточки "Сотрудник". Скрывает тайлы
"Копировать карточку" и "Создать шаблон", если пользователь не администратор и
не используется кастомная система прав доступа к карточке "Сотрудник".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PersonalRoleTileExtension : TileExtension
VB __Копировать
     Public NotInheritable Class PersonalRoleTileExtension
    	Inherits TileExtension
C++ __Копировать
     public ref class PersonalRoleTileExtension sealed : public TileExtension
F# __Копировать
     [<SealedAttribute>]
    type PersonalRoleTileExtension = 
        class
            inherit TileExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[TileExtension](T_Tessa_UI_Tiles_Extensions_TileExtension.htm) __ PersonalRoleTileExtension
##  __Конструкторы
[PersonalRoleTileExtension](M_Tessa_Extensions_Platform_Client_Tiles_PersonalRoleTileExtension__ctor.htm)|
Инициализирует новый экземпляр класса PersonalRoleTileExtension  
---|---  
##  __Методы
[ClosedLocal](M_Tessa_UI_Tiles_Extensions_TileExtension_ClosedLocal.htm)|
Выполняется после закрытия одной из панелей локальной рабочей области. При
этом используются те же экземпляры расширений, что и при открытии панели.  
(Унаследован от
[TileExtension](T_Tessa_UI_Tiles_Extensions_TileExtension.htm))  
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
[FinalizedLocal](M_Tessa_UI_Tiles_Extensions_TileExtension_FinalizedLocal.htm)|
Выполняется после того, как локальная рабочая область становится не нужна и
больше не будет использоваться. При этом используются те же экземпляры
расширений, что и при инициализации рабочей области.  
(Унаследован от
[TileExtension](T_Tessa_UI_Tiles_Extensions_TileExtension.htm))  
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
[InitializingGlobal](M_Tessa_UI_Tiles_Extensions_TileExtension_InitializingGlobal.htm)|
Выполняет добавление и настройку плиток в глобальной рабочей области.  
(Унаследован от
[TileExtension](T_Tessa_UI_Tiles_Extensions_TileExtension.htm))  
[InitializingLocal](M_Tessa_Extensions_Platform_Client_Tiles_PersonalRoleTileExtension_InitializingLocal.htm)|  
(Переопределяет
[TileExtension.InitializingLocal(ITileLocalExtensionContext)](M_Tessa_UI_Tiles_Extensions_TileExtension_InitializingLocal.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OpeningLocal](M_Tessa_UI_Tiles_Extensions_TileExtension_OpeningLocal.htm)|
Выполняет подготовку локальной рабочей области для отображения одной из её
панелей.  
(Унаследован от
[TileExtension](T_Tessa_UI_Tiles_Extensions_TileExtension.htm))  
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
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
