# PlaceholderDocumentBuilderFunc - делегат
Функция, создающая и возвращающая документ для заданного потока с содержимым
documentStream. Также возвращается функция getDocumentContentFunc, которая
получает контент изменённого документа в форме массива байт при успешной
замене плейсхолдеров.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IPlaceholderDocument PlaceholderDocumentBuilderFunc(
    	Guid templateCardID,
    	MemoryStream documentStream,
    	out Func<IPlaceholderDocument, byte[]> getDocumentContentFunc
    )
VB __Копировать
     Public Delegate Function PlaceholderDocumentBuilderFunc ( 
    	templateCardID As Guid,
    	documentStream As MemoryStream,
    	<OutAttribute> ByRef getDocumentContentFunc As Func(Of IPlaceholderDocument, Byte())
    ) As IPlaceholderDocument
C++ __Копировать
     public delegate IPlaceholderDocument^ PlaceholderDocumentBuilderFunc(
    	Guid templateCardID, 
    	MemoryStream^ documentStream, 
    	[OutAttribute] Func<IPlaceholderDocument^, array<unsigned char>^>^% getDocumentContentFunc
    )
F# __Копировать
     type PlaceholderDocumentBuilderFunc = 
        delegate of 
            templateCardID : Guid * 
            documentStream : MemoryStream * 
            getDocumentContentFunc : Func<IPlaceholderDocument, byte[]> byref -> IPlaceholderDocument
#### Параметры
templateCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки-шаблона, документ которой используется для замены плейсхолдеров. 
documentStream
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream)
     Поток файла документа, в котором должны быть заменены плейсхолдеры. Не может быть равен null. 
getDocumentContentFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IPlaceholderDocument](T_Tessa_Platform_Placeholders_IPlaceholderDocument.htm),
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
    Результат выполнения запроса. Не должен быть равен null.
#### Возвращаемое значение
[IPlaceholderDocument](T_Tessa_Platform_Placeholders_IPlaceholderDocument.htm)  
Документ, для которого выполняется замена плейсхолдеров.
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
