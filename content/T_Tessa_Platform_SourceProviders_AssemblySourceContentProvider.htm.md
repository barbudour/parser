# AssemblySourceContentProvider - класс
Провайдер для источника, представляющего собой конкретный ресурс. Например,
файл и т.п.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AssemblySourceContentProvider : AssemblySourceProviderBase, 
    	ISourceContentProvider, ISourceProviderBase
VB __Копировать
     Public Class AssemblySourceContentProvider
    	Inherits AssemblySourceProviderBase
    	Implements ISourceContentProvider, ISourceProviderBase
C++ __Копировать
     public ref class AssemblySourceContentProvider : public AssemblySourceProviderBase, 
    	ISourceContentProvider, ISourceProviderBase
F# __Копировать
     type AssemblySourceContentProvider = 
        class
            inherit AssemblySourceProviderBase
            interface ISourceContentProvider
            interface ISourceProviderBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm) __[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm) __ AssemblySourceContentProvider
Implements
    [ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm), [ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm)
##  __Конструкторы
[AssemblySourceContentProvider](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider__ctor.htm)|
Создает экземпляр провайдера для конкретного файла в сборке.  
---|---  
## __Свойства
[Assembly](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_Assembly.htm)|
Сборка, содержащая ресурсы.  
(Унаследован от
[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm))  
---|---  
[DirectoryPath](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_DirectoryPath.htm)|
Путь до ресурса относительно сборки.  
(Унаследован от
[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm))  
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm)|
Флаг указывает на то, что источник предназначен только для чтения. Зависит от
реализаций провайдеров.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
##  __Методы
[CheckReadOnly](M_Tessa_Platform_SourceProviders_SourceProviderBase_CheckReadOnly.htm)|
Проверяет, является ли объект доступен только для чтения
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm),
и выбрасывает исключение, если является.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
---|---  
[CreateStreamReadAsync](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_CreateStreamReadAsync.htm)|
Получает поток контента для чтения ресурса, который представляет данный
провайдер.  
[CreateStreamWriteAsync](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_CreateStreamWriteAsync.htm)|
Получает поток контента для записи или создания ресурса, который представляет
данный провайдер.  
[DeleteAsync](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_DeleteAsync.htm)|
Позволяет удалить источник, для которого предназначен провайдер.  
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
[GetCachedNamesList](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_GetCachedNamesList.htm)|
Возвращает кэшированный список ресурсов расположенные в сборке по пути
[DirectoryPath](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_DirectoryPath.htm).  
(Унаследован от
[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm))  
[GetCurrentDirectoryProvider](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_GetCurrentDirectoryProvider.htm)|
Получает провайдер для текущей директории ресурса.  
[GetFullName](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_GetFullName.htm)|
Возвращает абсолютный путь к ресурсу.  
(Переопределяет
[SourceProviderBase.GetFullName()](M_Tessa_Platform_SourceProviders_SourceProviderBase_GetFullName.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNameWithoutDirectoryPath](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_GetNameWithoutDirectoryPath.htm)|
Получает простое имя ресурса, который представляет данный провайдер. Например,
имя файла без остального пути и т.п.  
[GetResourcePath](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_GetResourcePath.htm)|  
(Переопределяет
[AssemblySourceProviderBase.GetResourcePath()](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_GetResourcePath.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_IsExistsAsync.htm)|
Получает значение, показывающее существует ли источник для которого
предназначен текущий провайдер.  
(Переопределяет
[SourceProviderBase.IsExistsAsync(CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderBase_IsExistsAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Platform_SourceProviders_AssemblySourceContentProvider_ToString.htm)|
Returns a string that represents the current object.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
