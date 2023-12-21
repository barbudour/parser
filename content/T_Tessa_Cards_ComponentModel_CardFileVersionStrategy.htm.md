# CardFileVersionStrategy - класс
Стратегия, загружающая информацию по версиям файла и устанавливающая состояние
версии файла.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileVersionStrategy : ICardFileVersionStrategy
VB __Копировать
     Public NotInheritable Class CardFileVersionStrategy
    	Implements ICardFileVersionStrategy
C++ __Копировать
     public ref class CardFileVersionStrategy sealed : ICardFileVersionStrategy
F# __Копировать
     [<SealedAttribute>]
    type CardFileVersionStrategy = 
        class
            interface ICardFileVersionStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFileVersionStrategy
Implements
    [ICardFileVersionStrategy](T_Tessa_Cards_ComponentModel_ICardFileVersionStrategy.htm)
##  __Конструкторы
[CardFileVersionStrategy](M_Tessa_Cards_ComponentModel_CardFileVersionStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
---|---  
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
[GetVersionAsync](M_Tessa_Cards_ComponentModel_CardFileVersionStrategy_GetVersionAsync.htm)|
Возвращает общую информацию по версии файла с заданным идентификатором.  
[GetVersionsAsync](M_Tessa_Cards_ComponentModel_CardFileVersionStrategy_GetVersionsAsync.htm)|
Возвращает список с общей информацией по версиям файла с заданным
идентификатором.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetUploadErrorAsync](M_Tessa_Cards_ComponentModel_CardFileVersionStrategy_SetUploadErrorAsync.htm)|
Устанавливает, что загрузка контента для версии файла с заданным
идентификатором произошла с ошибкой.  
[SetUploadSuccessfulAsync](M_Tessa_Cards_ComponentModel_CardFileVersionStrategy_SetUploadSuccessfulAsync.htm)|
Устанавливает, что загрузка контента для версии файла с заданным
идентификатором была успешно завершена.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetContentHashAsync](M_Tessa_Cards_ComponentModel_CardFileVersionStrategy_TryGetContentHashAsync.htm)|
Возвращает хеш контента для версии файла с заданным идентификатором. Хеш может
быть равен null, если версия не найдена или её хеш не был рассчитан.  
## __Методы расширения
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
