# CardManager - класс
Объект, управляющий операциями с карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardManager : ICardManager
VB __Копировать
     Public NotInheritable Class CardManager
    	Implements ICardManager
C++ __Копировать
     public ref class CardManager sealed : ICardManager
F# __Копировать
     [<SealedAttribute>]
    type CardManager = 
        class
            interface ICardManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardManager
Implements
    [ICardManager](T_Tessa_Cards_ICardManager.htm)
##  __Конструкторы
[CardManager](M_Tessa_Cards_CardManager__ctor.htm)|  Создаёт экземпляр класса
с указанием репозитория карточек, используемого для выполнения операций с
карточками.  
---|---  
## __Методы
[CreateFromTemplateAsync(ISourceContentProvider,
Func<CardFileContentParameter, ValueTask>, Dictionary<String, Object>,
CardFileFormat,
CancellationToken)](M_Tessa_Cards_CardManager_CreateFromTemplateAsync_1.htm)|
Создаёт карточку по шаблону.  
---|---  
[CreateFromTemplateAsync(CardStoreRequest, CardHeader, Func<Int64,
CancellationToken, ValueTask<SubStream>>, Func<CardFileContentParameter,
ValueTask>, Dictionary<String, Object>, ICardFileSourceMapping,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardManager_CreateFromTemplateAsync.htm)|
Создаёт карточку по шаблону.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExportAsync(CardGetRequest, CardFileFormat,
CancellationToken)](M_Tessa_Cards_CardManager_ExportAsync.htm)|  Выполняет
административный экспорт карточки с файлами и заданиями, но не загружает
контент файлов.  
[ExportAsync(CardGetRequest, ISourceContentProvider, Dictionary<String,
Object>, CardFileFormat, IReadOnlyCollection<IStorageContentMapping>, Boolean,
CancellationToken)](M_Tessa_Cards_CardManager_ExportAsync_1.htm)|  Выполняет
административный экспорт карточки со всем её содержимым, включая файлы и
задания.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetExportedCardAsync](M_Tessa_Cards_CardManager_GetExportedCardAsync.htm)|
Загружает карточку, которая была экспортирована в файл.  
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
[ImportAsync(ISourceContentProvider, Dictionary<String, Object>,
CardFileFormat, Card, ICardMergeOptions, ILogger, Func<String, Boolean>,
Boolean, CancellationToken)](M_Tessa_Cards_CardManager_ImportAsync_1.htm)|
Выполняет административный импорт карточки со всем её содержимым, включая
файлы и задания.  
[ImportAsync(CardStoreRequest, CardHeader,
IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>>,
Dictionary<String, Object>, CardFileFormat, Card, ICardMergeOptions, ILogger,
Boolean, CancellationToken)](M_Tessa_Cards_CardManager_ImportAsync.htm)|
Выполняет административный импорт карточки со всем её содержимым, включая
файлы и задания.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareCardInTemplateForEditingAsync](M_Tessa_Cards_CardManager_PrepareCardInTemplateForEditingAsync.htm)|
Подготавливает карточку в шаблоне, десериализованную из шаблона, к
редактированию.  
[PrepareCardInTemplateForStoringAsync](M_Tessa_Cards_CardManager_PrepareCardInTemplateForStoringAsync.htm)|
Подготавливает отредактированную карточку в шаблоне для сериализации и
сохранения в шаблоне.  
[ReadExportedRequestAsync](M_Tessa_Cards_CardManager_ReadExportedRequestAsync.htm)|
Выполняет чтение запроса на импорт карточки из потока, содержащего
экспортированную карточку.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
