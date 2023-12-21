# Tessa.Platform.IO - пространство имён
Вспомогательные классы для работы с потоками или устройствами ввода / вывода.
##  __Классы
[CsvWriter](T_Tessa_Platform_IO_CsvWriter.htm)|  Объект осуществляющий запись
в csv  
---|---  
[DelegateReaderStream](T_Tessa_Platform_IO_DelegateReaderStream.htm)|  Поток,
чтение из которого делегируется заданной функции. Не поддерживает запись в
поток и свободное перемещение по нему при чтении [Seek(Int64,
SeekOrigin)](M_Tessa_Platform_IO_DelegateReaderStream_Seek.htm), но возвращает
размер [Length](P_Tessa_Platform_IO_DelegateReaderStream_Length.htm) и текущее
местоположение
[Position](P_Tessa_Platform_IO_DelegateReaderStream_Position.htm).  
[EncodingTranslatorStream](T_Tessa_Platform_IO_EncodingTranslatorStream.htm)|
This class is a stream designed to perform character encoding translation from
one encoding to another.  
[FileHelper](T_Tessa_Platform_IO_FileHelper.htm)|  Вспомогательные методы для
взаимодействия с файлами.  
[FileSpecialNames](T_Tessa_Platform_IO_FileSpecialNames.htm)|  Специальные
имена файлов, используемые системой.  
[HashingStream](T_Tessa_Platform_IO_HashingStream.htm)|  Поток для вычисления
хеш-функции от входящего потока по завершению чтения. Не поддерживает запись.
Вызовите метод
[FinalizeHashing()](M_Tessa_Platform_IO_HashingStream_FinalizeHashing.htm)
после того, как закончилось чтение из стрима, но перед тем, как будет получена
хеш-сумма из объекта-алгоритма
[ICryptoTransform](https://learn.microsoft.com/dotnet/api/system.security.cryptography.icryptotransform).  
[IndentedTextWriter](T_Tessa_Platform_IO_IndentedTextWriter.htm)|  
[IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm)|  Методы-расширения для
пространства имён Tessa.Platform.IO.  
[ProxyStream](T_Tessa_Platform_IO_ProxyStream.htm)|  Поток, который
оборачивает заданный оригинальный поток. Используется для случаев, когда API
некорректно обрабатывает оригинальный поток.  
[SeekableStream](T_Tessa_Platform_IO_SeekableStream.htm)|  Поток, который
оборачивает заданный оригинальный поток таким образом, чтобы всегда возвращать
[CanSeek](P_Tessa_Platform_IO_SeekableStream_CanSeek.htm), равный true, и
позволять выполнять переход на текущую позицию (например, если мы находимся в
позиции 0 и переходим на позицию 0).  
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm)|
Обеспечивает чтение сериализуемых объектов из потока.  
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm)|
Обеспечивает запись сериализуемых объектов в поток.  
[StreamHelper](T_Tessa_Platform_IO_StreamHelper.htm)|  Вспомогательные методы
и константы для организации работы с потоками ввода / вывода.  
[StringBuilderReader](T_Tessa_Platform_IO_StringBuilderReader.htm)|  
[SubStream](T_Tessa_Platform_IO_SubStream.htm)|  Поток, позволяющий
последовательно прочитать заданное число байт из заданного потока.  
[SuperStream](T_Tessa_Platform_IO_SuperStream.htm)|  Объект, предназначенный
для объединения нескольких объектов
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream) в
единственный байтовый поток, доступный только для чтения.  
[SuperStreamReader](T_Tessa_Platform_IO_SuperStreamReader.htm)|  Обеспечивает
чтение данных из суперпотока.  
[SuperStreamWriter](T_Tessa_Platform_IO_SuperStreamWriter.htm)|  Позволяет
записывать данные в суперпоток.  
[TempFile](T_Tessa_Platform_IO_TempFile.htm)|  Класс, позволяющий создавать
временные файлы.  
[TextPartReader](T_Tessa_Platform_IO_TextPartReader.htm)|  Обеспечивает чтение
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm) из потока и добавление
их в контекст
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm)  
[TextPartWriter](T_Tessa_Platform_IO_TextPartWriter.htm)|  Обеспечивает запись
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm) из контекста
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm)
в поток  
[Utf8StringWriter](T_Tessa_Platform_IO_Utf8StringWriter.htm)|  Объект
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter),
выполняющий запись в кодировке UTF-8.  
## __Интерфейсы
[ICsvItemSeparator](T_Tessa_Platform_IO_ICsvItemSeparator.htm)|  Описание
интерфейса разделителя полей  
---|---  
[IEscapeableStreamWriter](T_Tessa_Platform_IO_IEscapeableStreamWriter.htm)|
Объект-наследник
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter),
поддерживающий управление экранированием записываемых строк.  
[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)|  Информация по временному
файлу.  
[ITempFolder](T_Tessa_Platform_IO_ITempFolder.htm)|  Информация по папке,
которая предоставляет быстрый доступ ко множеству временных файлов
[ITempFile](T_Tessa_Platform_IO_ITempFile.htm) с отличающимися в пределах этой
папки именами.  
## __Перечисления
[FileAccessState](T_Tessa_Platform_IO_FileAccessState.htm)|  Состояние файла,
который требуется открыть для чтения.  
---|---  
[FileSpecialFolder](T_Tessa_Platform_IO_FileSpecialFolder.htm)|  Тип
специальной папки, используемой в системе.  
[SerializableObjectFormat](T_Tessa_Platform_IO_SerializableObjectFormat.htm)|
Формат сериализации для объектов
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm) и
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm).
