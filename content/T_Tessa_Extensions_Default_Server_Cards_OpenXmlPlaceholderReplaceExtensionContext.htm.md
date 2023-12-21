# OpenXmlPlaceholderReplaceExtensionContext - класс
Базовый класс контекста обработки расширений
[IPlaceholderReplaceExtension](T_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension.htm)
в документах OpenXML
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class OpenXmlPlaceholderReplaceExtensionContext : PlaceholderReplaceExtensionContext
VB __Копировать
     Public MustInherit Class OpenXmlPlaceholderReplaceExtensionContext
    	Inherits PlaceholderReplaceExtensionContext
C++ __Копировать
     public ref class OpenXmlPlaceholderReplaceExtensionContext abstract : public PlaceholderReplaceExtensionContext
F# __Копировать
     [<AbstractClassAttribute>]
    type OpenXmlPlaceholderReplaceExtensionContext = 
        class
            inherit PlaceholderReplaceExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm) __ OpenXmlPlaceholderReplaceExtensionContext
Derived
[Tessa.Extensions.Default.Server.Cards.ExcelPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext.htm)
[Tessa.Extensions.Default.Server.Cards.WordPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_WordPlaceholderReplaceExtensionContext.htm)
##  __Конструкторы
[OpenXmlPlaceholderReplaceExtensionContext](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderReplaceExtensionContext__ctor.htm)|
Инициализирует новый экземпляр класса
OpenXmlPlaceholderReplaceExtensionContext  
---|---  
##  __Свойства
[CancellationToken](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
---|---  
[FindingContext](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_FindingContext.htm)|  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[GroupLevel](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GroupLevel.htm)|
Флаг определяет текущий уровень вложенности группы.  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Info](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Info.htm)|
Инфо контекста  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[IsGroup](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_IsGroup.htm)|
Флаг показывает, относится ли текущая обработка строки к обработке строки
группировки.  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Placeholder](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Placeholder.htm)|
Текущий плейсхолдер  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[PlaceholderText](P_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderReplaceExtensionContext_PlaceholderText.htm)|  
[PlaceholderValue](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_PlaceholderValue.htm)|
Текущее значение для замены в плейсхолдере  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[ReplacementContext](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_ReplacementContext.htm)|
Контекст замены плейсхолдеров  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Row](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Row.htm)|
Текущая строка  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Table](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Table.htm)|
Текущая таблица  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[ValidationResult](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_ValidationResult.htm)|
Результат валидации  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
##  __Методы
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
[GetPlaceholderValueAsync](M_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GetPlaceholderValueAsync.htm)|
Метод для получения значения плейсхолдера в виде
[PlaceholderValue](P_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtensionContext_PlaceholderValue.htm)  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[GetTextFromPlaceholderAsync](M_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GetTextFromPlaceholderAsync.htm)|
Метод для получения текста по плейсхолдеру  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValueFromPlaceholderAsync<T>](M_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GetValueFromPlaceholderAsync__1.htm)|
Метод для получения значения плейсхолдера  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
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
